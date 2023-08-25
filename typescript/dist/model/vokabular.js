export class Vokabular {
    constructor(rawRow) {
        const data = rawRow.split(Vokabular.DELIMITER);
        this.notation = data[0];
        this.title = data[1];
        this.description = data[2];
    }
}
Vokabular.DELIMITER = ";";
//# sourceMappingURL=vokabular.js.map