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
                    <q-btn-dropdown label="Actividades" no-caps>
                        <q-list>
                            <q-item
                                clickable
                                v-ripple
                                v-for="(link, i) in essentialLinks"
                                :key="i"
                                no-caps
                                @click="$router.push({ name: link.link })"
                                :flat="
                                    $router.currentRoute.value.name !==
                                    link.link
                                "
                            >
                                <!-- <q-item-section avatar>
                                    <q-avatar
                                        :icon="link.icon"
                                        color="primary"
                                        text-color="white"
                                    />
                                </q-item-section> -->

                                <q-item-section>
                                    <q-btn color="primary" no-caps align="left">
                                        <q-icon
                                            :name="link.icon"
                                            class="q-mr-md"
                                        />
                                        {{ $q.screen.gt.sm ? link.title : '' }}
                                    </q-btn>
                                </q-item-section>

                                <!-- <q-item-section>
                                    {{
                                        $q.screen.gt.sm ? link.title : ''
                                    }}
                                </q-item-section> -->
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

const linksList = [
    {
        title: 'Profesores',
        caption: 'quasar.dev',
        icon: 'face',
        link: 'professors',
    },
    {
        title: 'Carreras',
        caption: 'quasar.dev',
        icon: 'school',
        link: 'careers',
    },
    {
        title: 'Departamentos',
        caption: 'quasar.dev',
        icon: 'door_front',
        link: 'departments',
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
        icon: 'auto_stories',
        link: 'subject-plannings',
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
            essentialLinks: linksList,
            leftDrawerOpen,
            imageLogo,
            toggleLeftDrawer() {
                leftDrawerOpen.value = !leftDrawerOpen.value;
            },
        };
    },
});
</script>
