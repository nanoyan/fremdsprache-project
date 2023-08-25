export class Vokabular {
    title: string;
    notation: string;
    description: string;
    static DELIMITER = ";"

    constructor(rawRow: string) {
        const data = rawRow.split(Vokabular.DELIMITER);
        this.notation = data[0];
        this.title = data[1];
        this.description = data[2];
    }

    // constructor(public id: string, 
    //     public notation: string, 
    //     public title: string, 
    //     public description: string, 
    //     public children: Vokabular[]) {}

    // addChild(child: Vokabular): void {
    //     this.children.push(child);
    // }
}

