export interface LinkList {
    title: string;
    icon?: string;
    link?: string;
}

export interface GroupLinkList {
    header: LinkList;
    corpus: Array<LinkList>;
}
