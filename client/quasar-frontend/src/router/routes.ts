import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        component: () => import('layouts/MainLayout.vue'),
        children: [
            {
                path: '',
                name: 'home',
                component: () => import('pages/Index.vue'),
            },
            {
                path: 'professors',
                name: 'professors',
                component: () =>
                    import('src/pages/teachingAssignments/Professors.vue'),
            },
            {
                path: 'careers',
                name: 'careers',
                component: () =>
                    import('src/pages/teachingAssignments/Careers.vue'),
            },
            {
                path: 'class-types',
                name: 'class-types',
                component: () =>
                    import('src/pages/teachingAssignments/ClassTypes.vue'),
            },
            {
                path: 'time-periods',
                name: 'time-periods',
                component: () =>
                    import('src/pages/teachingAssignments/TimePeriods.vue'),
            },
            {
                path: 'study-plans',
                name: 'study-plans',
                component: () =>
                    import('src/pages/teachingAssignments/StudyPlans.vue'),
            },
            {
                path: 'semesters',
                name: 'semesters',
                component: () =>
                    import('src/pages/teachingAssignments/Semesters.vue'),
            },
            {
                path: 'teaching-groups',
                name: 'teaching-groups',
                component: () =>
                    import('src/pages/teachingAssignments/TeachingGroups.vue'),
            },
            {
                path: 'teaching-category',
                name: 'teaching-category',
                component: () =>
                    import(
                        'src/pages/teachingAssignments/TeachingCategory.vue'
                    ),
            },
            {
                path: 'carmen-table',
                name: 'carmen-table',
                component: () =>
                    import('src/pages/teachingAssignments/CarmenTable.vue'),
            },
            {
                path: 'scientific-degree',
                name: 'scientific-degree',
                component: () =>
                    import(
                        'src/pages/teachingAssignments/ScientificDegrees.vue'
                    ),
            },
            {
                path: 'departments',
                name: 'departments',
                component: () =>
                    import('src/pages/teachingAssignments/Departments.vue'),
            },
            {
                path: 'subjects',
                name: 'subjects',
                component: () =>
                    import('src/pages/teachingAssignments/Subjects.vue'),
            },
            {
                path: 'subject-plannings',
                name: 'subject-plannings',
                component: () =>
                    import(
                        'src/pages/teachingAssignments/SubjectPlannings.vue'
                    ),
            },
            {
                path: 'teaching-assignments',
                name: 'teaching-assignments',
                component: () =>
                    import(
                        'src/pages/teachingAssignments/TeachingAssignments.vue'
                    ),
            },
            {
                path: 'students',
                name: 'students',
                component: () =>
                    import('src/pages/thesisCommittee/Students.vue'),
            },
            {
                path: 'thesis',
                name: 'thesis',
                component: () => import('src/pages/thesisCommittee/Thesis.vue'),
            },
            {
                path: 'thesis-committee',
                name: 'thesis-committee',
                component: () =>
                    import('src/pages/thesisCommittee/ThesisCommittee.vue'),
            },
        ],
    },

    // Always leave this as last one,
    // but you can also remove it
    {
        path: '/:catchAll(.*)*',
        component: () => import('pages/ErrorNotFound.vue'),
    },
];

export default routes;
