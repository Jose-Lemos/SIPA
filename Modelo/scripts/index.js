const puppeteer = require('puppeteer');



const cookie = {
  name: 'eljoselemond',
  value: 'eljoselemond@gmail.com',
  domain: 'google.com.ar',
  path: '/',
  httpOnly: true,
  secure: true
}

//{executablePath: 'C:/Users/eljos/AppData/Local/Google/Chrome/Application/chrome'}


(async () => {
  const browser = await puppeteer.launch();
  const url = 'https://www.bas.ac.uk/';
  const page = await browser.newPage();
  await page.goto(url);
  //let cookieset = await page.cookies(url);
  //console.log(JSON.stringify(cookieset));


  await browser.close();
})();