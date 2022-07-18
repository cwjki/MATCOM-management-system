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
                component: () => import('pages/Professors.vue'),
            },
            {
                path: 'careers',
                name: 'careers',
                component: () => import('pages/Careers.vue'),
            },
            {
                path: 'class-types',
                name: 'class-types',
                component: () => import('pages/ClassTypes.vue'),
            },
            {
                path: 'time-periods',
                name: 'time-periods',
                component: () => import('pages/TimePeriods.vue'),
            },
            {
                path: 'teaching-category',
                name: 'teaching-category',
                component: () => import('pages/TeachingCategory.vue'),
            },
            {
                path: 'scientific-degree',
                name: 'scientific-degree',
                component: () => import('pages/ScientificDegree.vue'),
            },
            {
                path: 'departments',
                name: 'departments',
                component: () => import('pages/Departments.vue'),
            },
            {
                path: 'subjects',
                name: 'subjects',
                component: () => import('pages/Subjects.vue'),
            },
            {
                path: 'subject-plannings',
                name: 'subject-plannings',
                component: () => import('pages/SubjectPlannings.vue'),
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
