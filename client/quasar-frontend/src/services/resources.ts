import { CareerModel } from 'src/models/career.model';
import { CarmenTableModel } from 'src/models/carmenTable.model';
import { DepartmentModel } from 'src/models/department.model';
import { ProfessorModel } from 'src/models/professor.model';
import { SubjectModel } from 'src/models/subject.model';
import { SubjectDescriptionModel } from 'src/models/subjectDescription.model';
import { TeachingAssignmentModel } from 'src/models/teachingAssignment.model';
import { CrudServiceFactory } from './api.service';

export const RESOURCES = {
    profesors: '/professors/',
    careers: '/careers/',
    departments: '/departments/',
    subjects: '/subjects/',
    subjectDescriptions: '/subject-descriptions/',
    teachingAssignment: '/teaching-assignments/',
    carmenTable: '/carmen-table/',
};

export const careerService = CrudServiceFactory<CareerModel>(RESOURCES.careers);

export const professorService = CrudServiceFactory<ProfessorModel>(
    RESOURCES.profesors
);

export const subjectService = CrudServiceFactory<SubjectModel>(
    RESOURCES.subjects
);

export const departmentService = CrudServiceFactory<DepartmentModel>(
    RESOURCES.departments
);

export const subjectDescriptionService =
    CrudServiceFactory<SubjectDescriptionModel>(RESOURCES.subjectDescriptions);

export const teachingAssignmentService =
    CrudServiceFactory<TeachingAssignmentModel>(RESOURCES.teachingAssignment);

export const carmenTableService = CrudServiceFactory<CarmenTableModel>(
    RESOURCES.carmenTable
);
