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
                path: 'docs',
                name: 'docs',
                component: () => import('pages/Docs.vue'),
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
                path: 'departments',
                name: 'departments',
                component: () => import('pages/Departments.vue'),
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
