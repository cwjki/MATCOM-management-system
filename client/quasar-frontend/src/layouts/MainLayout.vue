<template>
    <q-layout view="lHh Lpr lFf">
        <q-header elevated>
            <q-toolbar>
                <q-btn
                    flat
                    dense
                    round
                    v-if="$q.screen.xs"
                    :icon="'menu'"
                    class="q-mr-sm"
                    aria-label="Menu"
                    @click="toggleLeftDrawer"
                />

                <q-avatar @click="$router.push({ name: 'home' })">
                    <img :src="imageLogo" />
                </q-avatar>

                <q-toolbar-title @click="$router.push({ name: 'home' })">
                    Matcom
                </q-toolbar-title>

                <q-btn
                    label="Página Principal"
                    icon="home"
                    no-caps
                    @click="$router.push({ name: 'home' })"
                />

                <div>
                    <q-btn-dropdown label="Nomencladores" no-caps>
                        <q-list>
                            <q-item
                                clickable
                                v-ripple
                                v-for="(link, i) in essentialLinks1"
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

                <div>
                    <q-btn-dropdown label="Actividades" no-caps>
                        <q-list>
                            <q-item
                                clickable
                                v-ripple
                                v-for="(link, i) in essentialLinks2"
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

                <div>
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
            <q-list>
                <EssentialLink
                    v-for="link in essentialLinks"
                    :key="link.title"
                    v-bind="link"
                />
            </q-list>
        </q-drawer> -->

        <q-page-container>
            <router-view />
        </q-page-container>
    </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import EssentialLink from 'components/EssentialLink.vue';

const dropdownList1 = [
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
        title: 'Categorías Escolares',
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

const dropdownList2 = [
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
];

const thesisCommitteeLinks = [
    {
        title: 'Estudiantes',
        caption: 'quasar.dev',
        icon: 'door_front',
        link: 'students',
    },
];

export default defineComponent({
    name: 'MainLayout',

    components: {
        EssentialLink,
    },

    setup() {
        const leftDrawerOpen = ref(false);
        const imageLogo = require('src/assets/logo.jpg');
        return {
            essentialLinks1: dropdownList1,
            essentialLinks2: dropdownList2,
            thesisCommitteeLinks: thesisCommitteeLinks,
            leftDrawerOpen,
            imageLogo,
            toggleLeftDrawer() {
                leftDrawerOpen.value = !leftDrawerOpen.value;
            },
        };
    },
});
</script>
