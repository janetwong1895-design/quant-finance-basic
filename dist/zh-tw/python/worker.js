// Pinned runtime; work stays off the page's UI thread. No server-side execution.
const BASE='https://cdn.jsdelivr.net/pyodide/v314.0.7/full/';
let runtime,checkerGlobals,checker;
self.onmessage=async event=>{
 const {id,code,mode,cases,checkerSource}=event.data;
 let namespace;
 try{
  if(!runtime){
   self.postMessage({id,type:'loading'});
   const {loadPyodide}=await import(BASE+'pyodide.mjs');
   runtime=await loadPyodide({indexURL:BASE});
   runtime.setStdin({error:true});
   const dict=runtime.globals.get('dict');checkerGlobals=dict();dict.destroy();
   runtime.runPython(checkerSource,{globals:checkerGlobals});
   checker=checkerGlobals.get('run_checks');
  }
  let count=0,truncated=false;
  const stream=(text)=>{
   if(count>=12000){if(!truncated){self.postMessage({id,type:'output',text:'[Output capped at 12,000 characters.]\n'});truncated=true;}return;}
   const chunk=(String(text)+'\n').slice(0,12000-count);count+=chunk.length;
   self.postMessage({id,type:'output',text:chunk});
  };
  runtime.setStdout({batched:stream});runtime.setStderr({batched:stream});
  const dict=runtime.globals.get('dict');namespace=dict();dict.destroy();
  namespace.set('__name__',mode==='check'?'__practice__':'__main__');
  self.postMessage({id,type:'running'});
  const result=await runtime.runPythonAsync(code,{globals:namespace});
  if(result?.destroy)result.destroy();
  const results=mode==='check'?JSON.parse(checker(namespace,JSON.stringify(cases))):null;
  self.postMessage({id,type:'done',results,pythonVersion:runtime.runPython('import sys; sys.version.split()[0]')});
 }catch(error){self.postMessage({id,type:'error',text:String(error.message||error).slice(0,4000)});}
 finally{if(namespace)namespace.destroy();}
};
