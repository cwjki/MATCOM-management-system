<template>
    <q-layout view="lHh Lpr lFf">
        <q-header elevated>
            <q-toolbar>
                <!-- <q-btn
                    flat
                    dense
                    round
                    v-if="$q.screen.xs"
                    :icon="'menu'"
                    class="q-mr-sm"
                    aria-label="Menu"
                    @click="toggleLeftDrawer"
                /> -->

                <q-avatar
                    class="cursor-pointer"
                    @click="$router.push({ name: 'home' })"
                >
                    <img :src="imageLogo" />
                </q-avatar>

                <q-toolbar-title @click="$router.push({ name: 'home' })">
                    Matcom
                </q-toolbar-title>

                <div v-if="!$q.screen.lt.sm">
                    <q-btn-dropdown label="Datos generales" no-caps>
                        <q-list>
                            <q-item
                                clickable
                                v-ripple
                                v-for="(link, i) in teachingAssignmentLinks1"
                                :key="i"
                                no-caps
                                @click="$router.push({ name: link.link })"
                                :flat="
                                    $router.currentRoute.value.name !==
                                    link.link
                                "
                            >
                                <q-item-section>
                                    <q-btn color="primary" no-caps align="left">
                                        <q-icon
                                            :name="link.icon"
                                            class="q-mr-md"
                                        />
                                        {{ $q.screen.gt.sm ? link.title : '' }}
                                    </q-btn>
                                </q-item-section>
                            </q-item>
                        </q-list>
                    </q-btn-dropdown>
                </div>

                <div v-if="!$q.screen.lt.sm">
                    <q-btn-dropdown label="Asignación de Docencia" no-caps>
                        <q-list>
                            <q-item
                                clickable
                                v-ripple
                                v-for="(link, i) in teachingAssignmentLinks2"
                                :key="i"
                                no-caps
                                @click="$router.push({ name: link.link })"
                                :flat="
                                    $router.currentRoute.value.name !==
                                    link.link
                                "
                            >
                                <q-item-section>
                                    <q-btn color="primary" no-caps align="left">
                                        <q-icon
                                            :name="link.icon"
                                            class="q-mr-md"
                                        />
                                        {{ $q.screen.gt.sm ? link.title : '' }}
                                    </q-btn>
                                </q-item-section>
                            </q-item>
                        </q-list>
                    </q-btn-dropdown>
                </div>

                <div v-if="!$q.screen.lt.sm">
                    <q-btn-dropdown label="Tribunal de Tesis" no-caps>
                        <q-list>
                            <q-item
                                clickable
                                v-ripple
                                v-for="(link, i) in thesisCommitteeLinks"
                                :key="i"
                                no-caps
                                @click="$router.push({ name: link.link })"
                                :flat="
                                    $router.currentRoute.value.name !==
                                    link.link
                                "
                            >
                                <q-item-section>
                                    <q-btn color="primary" no-caps align="left">
                                        <q-icon
                                            :name="link.icon"
                                            class="q-mr-md"
                                        />
                                        {{ $q.screen.gt.sm ? link.title : '' }}
                                    </q-btn>
                                </q-item-section>
                            </q-item>
                        </q-list>
                    </q-btn-dropdown>
                </div>
            </q-toolbar>
        </q-header>

        <!-- <q-drawer v-model="leftDrawerOpen" bordered>
        </q-drawer> -->

        <q-page-container>
            <router-view :key="$router.currentRoute.value.fullPath" />
        </q-page-container>
    </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { GroupLinkData } from 'src/models/linkData';

const teachingAssignmentLinks1 = [
    {
        title: 'Facultades',
        caption: 'quasar.dev',
        icon: 'museum',
        link: 'faculties',
    },
    {
        title: 'Carreras',
        caption: 'quasar.dev',
        icon: 'school',
        link: 'careers',
    },
    {
        title: 'Actividades de clase',
        caption: 'quasar.dev',
        icon: 'class',
        link: 'class-types',
    },
    {
        title: 'Planes de estudio',
        caption: 'quasar.dev',
        icon: 'font_download',
        link: 'study-plans',
    },
    {
        title: 'Grupos',
        caption: 'quasar.dev',
        icon: 'groups',
        link: 'teaching-groups',
    },
    {
        title: 'Cursos Escolares',
        caption: 'quasar.dev',
        icon: 'date_range',
        link: 'scholar-years',
    },
    {
        title: 'Períodos de tiempo',
        caption: 'quasar.dev',
        icon: 'date_range',
        link: 'time-periods',
    },
    {
        title: 'Semestres',
        caption: 'quasar.dev',
        icon: 'calendar_month',
        link: 'semesters',
    },
    {
        title: 'Categorías Docentes',
        caption: 'quasar.dev',
        icon: 'star_rate',
        link: 'teaching-category',
    },
    {
        title: 'Grados Científicos',
        caption: 'quasar.dev',
        icon: 'stars',
        link: 'scientific-degree',
    },
];

const teachingAssignmentLinks2 = [
    {
        title: 'Departamentos',
        caption: 'quasar.dev',
        icon: 'door_front',
        link: 'departments',
    },
    {
        title: 'Tabla de Carmen',
        caption: 'quasar.dev',
        icon: 'calendar_view_week',
        link: 'carmen-table',
    },
    {
        title: 'Profesores',
        caption: 'quasar.dev',
        icon: 'face',
        link: 'professors',
    },
    {
        title: 'Asignaturas',
        caption: 'quasar.dev',
        icon: 'auto_stories',
        link: 'subjects',
    },
    {
        title: 'Planificación de Asignaturas',
        caption: 'quasar.dev',
        icon: 'feed',
        link: 'subject-plannings',
    },
    {
        title: 'Asignación de Docencia',
        caption: 'quasar.dev',
        icon: 'assignment_turned_in',
        link: 'teaching-assignments',
    },
    // {
    //     title: 'Planificación de Docencia',
    //     caption: 'quasar.dev',
    //     icon: 'assignment_turned_in',
    //     link: 'teaching-planning',
    // },
];

const thesisCommitteeLinks = [
    {
        title: 'Locales',
        caption: 'quasar.dev',
        icon: 'pin_drop',
        link: 'places',
    },
    {
        title: 'Palabras Claves',
        caption: 'quasar.dev',
        icon: 'manage_search',
        link: 'keywords',
    },
    {
        title: 'Tesis',
        caption: 'quasar.dev',
        icon: 'description',
        link: 'thesis',
    },
    {
        title: 'Tribunal de Tesis',
        caption: 'quasar.dev',
        icon: 'groups',
        link: 'thesis-committees',
    },
    {
        title: 'Defensas de Tesis',
        caption: 'quasar.dev',
        icon: 'calendar_month',
        link: 'thesis-defenses',
    },
];

const linksData: Array<GroupLinkData> = [
    {
        data: {
            title: 'Datos generales',
        },
        childLinks: [
            {
                data: {
                    title: 'Facultad',
                },
                childLinks: [
                    {
                        data: {
                            title: 'Facultades',
                            icon: 'museum',
                            link: 'faculties',
                        },
                    },
                    {
                        data: {
                            title: 'Carreras',
                            icon: 'school',
                            link: 'careers',
                        },
                    },
                    {
                        data: {
                            title: 'Departamentos',
                            icon: 'door_front',
                            link: 'departments',
                        },
                    },
                    {
                        data: {
                            title: 'Profesores',
                            icon: 'face',
                            link: 'professors',
                        },
                        childLinks: [
                            {
                                data: {
                                    title: 'Categorías Docentes',
                                    icon: 'star_rate',
                                    link: 'teaching-category',
                                },
                            },
                            {
                                data: {
                                    title: 'Grados Científicos',
                                    icon: 'stars',
                                    link: 'scientific-degree',
                                },
                            },
                        ],
                    },
                    {
                        data: {
                            title: 'Locales',
                            icon: 'pin_drop',
                            link: 'places',
                        },
                    },
                ],
            },
            {
                data: {
                    title: 'Curso escolar',
                },
                childLinks: [
                    {
                        data: {
                            title: 'Cursos Escolares',
                            icon: 'date_range',
                            link: 'scholar-years',
                        },
                    },
                    {
                        data: {
                            title: 'Planes de estudio',
                            icon: 'font_download',
                            link: 'study-plans',
                        },
                    },
                    {
                        data: {
                            title: 'Grupos',
                            icon: 'groups',
                            link: 'teaching-groups',
                        },
                    },
                    {
                        data: {
                            title: 'Períodos de tiempo',
                            icon: 'date_range',
                            link: 'time-periods',
                        },
                    },
                    {
                        data: {
                            title: 'Semestres',
                            icon: 'calendar_month',
                            link: 'semesters',
                        },
                    },
                    {
                        data: {
                            title: 'Actividades de clase',
                            icon: 'class',
                            link: 'class-types',
                        },
                    },
                ],
            },
        ],
    },
    {
        data: {
            title: 'Asignación de docencia',
        },
        childLinks: [
            {
                data: {
                    title: 'Detalles de años',
                    icon: 'calendar_view_week',
                    link: 'carmen-table',
                },
            },
            {
                data: {
                    title: 'Asignaturas',
                    icon: 'auto_stories',
                    link: 'subjects',
                },
            },
            {
                data: {
                    title: 'Carga de las asignaturas',
                    icon: 'feed',
                    link: 'subject-plannings',
                },
            },
            {
                data: {
                    title: 'Asignación de Docencia',
                    icon: 'assignment_turned_in',
                    link: 'teaching-assignments',
                },
            },
        ],
    },
    {
        data: {
            title: 'Planificación de las tesis',
        },
        childLinks: [
            {
                data: {
                    title: 'Palabras Claves',
                    icon: 'manage_search',
                    link: 'keywords',
                },
            },
            {
                data: {
                    title: 'Tesis',
                    icon: 'description',
                    link: 'thesis',
                },
            },
            {
                data: {
                    title: 'Tribunal de Tesis',
                    icon: 'groups',
                    link: 'thesis-committees',
                },
            },
            {
                data: {
                    title: 'Defensas de Tesis',
                    icon: 'calendar_month',
                    link: 'thesis-defenses',
                },
            },
        ],
    },
];

export default defineComponent({
    name: 'MainLayout',

    setup() {
        const leftDrawerOpen = ref(false);
        const imageLogo = require('src/assets/logo.jpg');
        return {
            teachingAssignmentLinks1: teachingAssignmentLinks1,
            teachingAssignmentLinks2: teachingAssignmentLinks2,
            thesisCommitteeLinks: thesisCommitteeLinks,
            linksData,
            leftDrawerOpen,
            imageLogo,
            toggleLeftDrawer() {
                leftDrawerOpen.value = !leftDrawerOpen.value;
            },
        };
    },
});
</script>
