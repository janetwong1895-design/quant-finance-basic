import {readFileSync,writeFileSync} from 'node:fs';
for(let n=1;n<=10;n++){
 const path=new URL(n===1?'../dist/index.html':`../dist/chapter-${String(n).padStart(2,'0')}/index.html`,import.meta.url);
 let text=readFileSync(path,'utf8');
 const source=n===1?'course-navigation.mjs':'../course-navigation.mjs';
 if(!text.includes(`src="${source}"`))text=text.replace('</head>',`<script type="module" src="${source}"></script></head>`);
 writeFileSync(path,text);
}
console.log('All chapter selectors and course links use the ten-chapter navigation.');
