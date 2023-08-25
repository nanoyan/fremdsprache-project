function readCSVFile(filePath) {
    const results = [];
    const path = require('path');
    const csvFilePath = path.resolve(filePath);
    const fs = require('fs');
    const headers = ['notation', 'title', 'description'];
    const fileContent = fs.readFileSync(csvFilePath, { encoding: 'utf-8' });
    const parse = require('csv-parse');
    parse.parse(fileContent, {
        delimiter: ';',
        columns: headers,
    }, (error, result) => {
        if (error) {
            console.error(error);
        }
        console.log("Result", result);
    });
}
readCSVFile('../../../fremdsprache/original-data/esa-text.csv');
export {};
//# sourceMappingURL=json_creator.js.map