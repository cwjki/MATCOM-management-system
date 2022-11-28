export interface LinkData {
    title: string;
    icon?: string;
    link?: string;
    outline?: boolean;
}

export interface GroupLinkData {
    data: LinkData;
    childLinks?: Array<GroupLinkData>;
}
