import { CareerModel } from 'src/models/career.model';
import { CarmenTableModel } from 'src/models/carmenTable.model';
import { DepartmentModel } from 'src/models/department.model';
import { ProfessorModel } from 'src/models/professor.model';
import { ScientificDegreeModel } from 'src/models/scientificDegree.model';
import { SemesterModel } from 'src/models/semester.model';
import { ClassTypeModel } from 'src/models/classType.model';
import { TimePeriodModel } from 'src/models/timePeriod.model';
import { StudyPlanModel } from 'src/models/studyPlan.model';
import { SubjectModel } from 'src/models/subject.model';
import { SubjectDescriptionModel } from 'src/models/subjectDescription.model';
import { TeachingAssignmentModel } from 'src/models/teachingAssignment.model';
import { TeachingCategoryModel } from 'src/models/teachingCategory.model';
import { CrudServiceFactory } from './api.service';
import { TeachingGroupModel } from 'src/models/teachingGroup.model';

export const RESOURCES = {
    profesors: '/professors/',
    careers: '/careers/',
    departments: '/departments/',
    subjects: '/subjects/',
    subjectDescriptions: '/subject-descriptions/',
    teachingAssignments: '/teaching-assignments/',
    carmenTable: '/carmen-table/',
    teachingCategory: '/teaching-categories/',
    scientificDegree: '/scientific-degrees/',
    semesters: '/semesters/',
    studyPlans: '/study-plans/',
    classTypes: '/class-types/',
    timePeriods: '/time-periods/',
    teachingGroups: '/teaching-groups/',
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
    CrudServiceFactory<TeachingAssignmentModel>(RESOURCES.teachingAssignments);

export const carmenTableService = CrudServiceFactory<CarmenTableModel>(
    RESOURCES.carmenTable
);

export const teachingCategoryService =
    CrudServiceFactory<TeachingCategoryModel>(RESOURCES.teachingCategory);

export const scientificDegreeService =
    CrudServiceFactory<ScientificDegreeModel>(RESOURCES.scientificDegree);

export const studyPlanService = CrudServiceFactory<StudyPlanModel>(
    RESOURCES.studyPlans
);

export const semesterService = CrudServiceFactory<SemesterModel>(
    RESOURCES.semesters
);

export const classTypeService = CrudServiceFactory<ClassTypeModel>(
    RESOURCES.classTypes
);

export const timePeriodService = CrudServiceFactory<TimePeriodModel>(
    RESOURCES.timePeriods
);

export const teachingGroupService = CrudServiceFactory<TeachingGroupModel>(
    RESOURCES.teachingGroups
);
