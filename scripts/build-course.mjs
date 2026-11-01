import {spawnSync} from 'node:child_process';
const steps=[[process.execPath,'scripts/build-guides.mjs'],['python3','scripts/build-python-practice.py'],[process.execPath,'scripts/build-course-navigation.mjs'],[process.execPath,'scripts/build-landing.mjs'],[process.execPath,'scripts/build-zh-tw.mjs']];
for(const [command,...args]of steps){const result=spawnSync(command,args,{stdio:'inherit'});if(result.status!==0)process.exit(result.status||1);}
