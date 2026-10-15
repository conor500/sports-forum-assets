const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:600,height:800},deviceScaleFactor:2});
for(const n of process.argv.slice(2)){await p.goto('file://'+__dirname+'/'+n+'.html');await (await p.$('#c')).screenshot({path:__dirname+'/'+n+'.png'});}
await b.close()})();
