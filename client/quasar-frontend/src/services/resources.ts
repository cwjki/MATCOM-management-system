import { CareerModel } from 'src/models/teachingAssignments/career.model';
import { CarmenTableModel } from 'src/models/teachingAssignments/carmenTable.model';
import { DepartmentModel } from 'src/models/teachingAssignments/department.model';
import { ProfessorModel } from 'src/models/teachingAssignments/professor.model';
import { ScientificDegreeModel } from 'src/models/teachingAssignments/scientificDegree.model';
import { SemesterModel } from 'src/models/teachingAssignments/semester.model';
import { ClassTypeModel } from 'src/models/teachingAssignments/classType.model';
import { TimePeriodModel } from 'src/models/teachingAssignments/timePeriod.model';
import { StudyPlanModel } from 'src/models/teachingAssignments/studyPlan.model';
import { SubjectModel } from 'src/models/teachingAssignments/subject.model';
import { SubjectDescriptionModel } from 'src/models/teachingAssignments/subjectDescription.model';
import { TeachingAssignmentModel } from 'src/models/teachingAssignments/teachingAssignment.model';
import { TeachingPlanningModel } from 'src/models/teachingAssignments/teachingPlanning.model';
import { TeachingCategoryModel } from 'src/models/teachingAssignments/teachingCategory.model';
import { TeachingGroupModel } from 'src/models/teachingAssignments/teachingGroup.model';
import { StudentModel } from 'src/models/thesisCommittee/students.model';
import { ThesisModel } from 'src/models/thesisCommittee/thesis.model';
import { ThesisCommitteeModel } from 'src/models/thesisCommittee/thesisCommittee.model';
import { CrudServiceFactory } from './api.service';
import { FacultyModel } from 'src/models/teachingAssignments/faculty.model';

export const RESOURCES = {
    profesors: '/professors/',
    faculties: '/faculties/',
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
    teachingAssignment: '/teaching-assignments/',
    teachingPlanning: 'teaching-planning',

    students: '/students/',
    thesis: '/thesis/',
    thesisCommittee: '/thesis-committee/',
};

export const careerService = CrudServiceFactory<CareerModel>(RESOURCES.careers);

export const professorService = CrudServiceFactory<ProfessorModel>(
    RESOURCES.profesors
);

export const subjectService = CrudServiceFactory<SubjectModel>(
    RESOURCES.subjects
);

export const facultyService = CrudServiceFactory<FacultyModel>(
    RESOURCES.faculties
);

export const departmentService = CrudServiceFactory<DepartmentModel>(
    RESOURCES.departments
);

export const subjectDescriptionService =
    CrudServiceFactory<SubjectDescriptionModel>(RESOURCES.subjectDescriptions);

export const teachingAssignmentService =
    CrudServiceFactory<TeachingAssignmentModel>(RESOURCES.teachingAssignments);

export const teachingPlanningService =
    CrudServiceFactory<TeachingPlanningModel>(RESOURCES.teachingPlanning);

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

export const studentService = CrudServiceFactory<StudentModel>(
    RESOURCES.students
);

export const thesisService = CrudServiceFactory<ThesisModel>(RESOURCES.thesis);

export const thesisCommitteeService = CrudServiceFactory<ThesisCommitteeModel>(
    RESOURCES.thesisCommittee
);
