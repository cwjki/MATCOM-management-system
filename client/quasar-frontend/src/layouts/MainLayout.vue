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

                <div>
                    <q-btn
                        v-for="(link, i) in essentialLinks"
                        :key="i"
                        :label="link.title"
                        :icon="link.icon"
                        no-caps
                        @click="$router.push({ name: link.link })"
                        :flat="$router.currentRoute.value.name !== link.link"
                    />
                </div>
            </q-toolbar>
        </q-header>

        <q-drawer v-model="leftDrawerOpen" bordered>
            <q-list>
                <EssentialLink
                    v-for="link in essentialLinks"
                    :key="link.title"
                    v-bind="link"
                />
            </q-list>
        </q-drawer>

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
        title: 'Docs',
        caption: 'quasar.dev',
        icon: 'school',
        link: 'docs',
    },
    {
        title: 'Home',
        caption: 'quasar.dev',
        icon: 'home',
        link: 'home',
    },
    {
        title: 'Profesores',
        caption: 'quasar.dev',
        icon: 'face',
        link: 'professors',
    },
    {
        title: 'Carreras',
        caption: 'quasar.dev',
        icon: 'face',
        link: 'careers',
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
