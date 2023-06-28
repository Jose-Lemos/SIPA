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

/* global bootstrap: false */
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()

const content_form = document.getElementsByClassName("content-form");

document.getElementById("btn-selec").addEventListener("click", ()=>{
  content_form.classList.add("content-form-toggle")
});


var html_extract = document.getElementById("container-html-extract");

String.prototype.allIndexesOf = function(c, n) {
  var indexes = [];
  n = n || 0;
  while ((n = this.indexOf(c, n)) >= 0) {
  indexes.push(n++);
  }
  return indexes;
}

function cargarArticulosExtraidos(art_text){
  art_string = String(art_text);
  puntos_coma = art_string.allIndexesOf(";");

  for (elem in puntos_coma){
    var pi = "";
    
  }
}