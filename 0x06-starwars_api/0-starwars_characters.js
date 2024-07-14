#!/usr/bin/node
// star wars api
const reques = require('request');
const util = require('util');
const request = util.promisify(reques);

async function star (url) {
  const body = await (await request(url)).body;
  const pot = JSON.parse(body);
  const people = pot.characters;
  for (const character of people) {
    const bod = await (await request(character)).body;
    const person = JSON.parse(bod);
    console.log(person.name);
  }
}

const value = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + value;
star(url);
