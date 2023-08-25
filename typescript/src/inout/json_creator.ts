import { Vokabular } from "../model/vokabular";

type Vokab = {
    notation: string;
    title: string;
    description: string;
}


function readCSVFile(filePath: string) {
    const results: object[] = [];
    const path = require ('path');
    const csvFilePath = path.resolve(filePath);
    const fs = require('fs')

    const headers = ['notation', 'title', 'description']
    const fileContent = fs.readFileSync(csvFilePath, { encoding: 'utf-8' }) 
    
    const parse = require('csv-parse');
    parse.parse(fileContent, {
        delimiter: ';',
        columns: headers,
    }, (error: any, result: Vokabular[]) => {
        if (error) {
            console.error(error);
        } 
        console.log("Result", result);
        

    });

}

readCSVFile('../../../fremdsprache/original-data/esa-text.csv')