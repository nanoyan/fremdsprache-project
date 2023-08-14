class Vocab {
    constructor(id: string, notation: string, title: string, description: string, children: Vocab[]) {
        this.id = id;
        this.notation = notation;
        this.title = title;
        this.description = description;
        this.children = children;
    }
    id: string;
    notation: string;
    title: string;
    description: string;
    children: Vocab[];

    addChild(child: Vocab): void {
        this.children.push(child);
    }
}