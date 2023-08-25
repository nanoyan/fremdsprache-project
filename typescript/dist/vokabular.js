export class Vokabular {
    constructor(notation, title, description) {
        this.notation = notation;
        this.title = title;
        this.description = description;
    }
    constructor(id, notation, title, description, children) {
        this.id = id;
        this.notation = notation;
        this.title = title;
        this.description = description;
        this.children = children;
    }
    addChild(child) {
        this.children.push(child);
    }
}
//# sourceMappingURL=vokabular.js.map