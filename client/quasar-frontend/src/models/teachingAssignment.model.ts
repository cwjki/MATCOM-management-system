export interface TeachingAssignmentModel {
    id: number;
    professor: string;
    subject: string;
    classType: string;
    timePeriod: string;
    numberOfHours: number;
    numberOfGroups: number;
    percent: number;
    group: number;
}
