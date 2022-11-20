import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        component: () => import('layouts/MainLayout.vue'),
        children: [
            {
                path: '',
                name: 'home',
                component: () => import('pages/NewIndex.vue'),
            },
            {
                path: 'professors',
                name: 'professors',
                component: () =>
                    import('src/pages/teachingAssignments/Professors.vue'),
            },
            {
                path: 'faculties',
                name: 'faculties',
                component: () =>
                    import('src/pages/teachingAssignments/Faculties.vue'),
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
                path: 'scholar-years',
                name: 'scholar-years',
                component: () =>
                    import('src/pages/teachingAssignments/ScholarYears.vue'),
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
                path: 'teaching-planning',
                name: 'teaching-planning',
                component: () =>
                    import(
                        'src/pages/teachingAssignments/TeachingPlanning.vue'
                    ),
            },
            {
                path: 'places',
                name: 'places',
                component: () => import('src/pages/thesisCommittee/Place.vue'),
            },
            {
                path: 'keywords',
                name: 'keywords',
                component: () =>
                    import('src/pages/thesisCommittee/Keyword.vue'),
            },
            {
                path: 'thesis/',
                name: 'thesis',
                component: () => import('src/pages/thesisCommittee/Thesis.vue'),
            },
            {
                path: 'thesis-committees',
                name: 'thesis-committees',
                component: () =>
                    import('src/pages/thesisCommittee/ThesisCommittee.vue'),
            },
            {
                path: 'thesis-defenses',
                name: 'thesis-defenses',
                component: () =>
                    import('src/pages/thesisCommittee/ThesisDefense.vue'),
            },
            {
                path: 'thesis/:idC/:Cname',
                props: true,
                name: 'thesis-id',
                component: () => import('src/pages/thesisCommittee/Thesis.vue'),
            },
            {
                path: 'thesis-committees/:idC/:Cname',
                props: true,
                name: 'thesis-committees-id',
                component: () =>
                    import('src/pages/thesisCommittee/ThesisCommittee.vue'),
            },
            {
                path: 'thesis-defenses/:idC/:Cname',
                props: true,
                name: 'thesis-defenses-id',
                component: () =>
                    import('src/pages/thesisCommittee/ThesisDefense.vue'),
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
