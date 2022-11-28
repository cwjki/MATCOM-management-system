<template>
    <q-page class="bgFond" padding>
        <!-- <q-img class="full-height full-width" :src="imageBg"></q-img> -->
        <div flat class="row full-width justify-evenly items-start">
            <q-card class="col-12 bg-custom-grey-card row q-pa-md">
                <q-card-section class="col-md-6 col-sm-8 col-11">
                    <div class="text-h4 text-bold q-pb-sm">
                        SISTEMA DE GESTIÓN DOCENTE
                    </div>
                    <q-separator></q-separator>

                    <div class="text-subtitle1 q-pt-md">
                        para la facultad de Matemática y Computación de la UH
                    </div>
                </q-card-section>
            </q-card>
            <q-card
                :class="`bg-custom-card row justify-center col-md-9 col-sm-8 col-12 q-mt-lg ${
                    $q.screen.xs || 'q-pa-md'
                }`"
            >
                <q-card-section class="col-12 q-pb-none">
                    <p class="text-h5 text-bold full-width">
                        Administración de departamentos
                    </p>
                    <!-- <p class="text-subtitle2 text-grey-6 full-width">MATCOM</p> -->
                </q-card-section>
                <div
                    class="col-md-6 col-12 q-pa-md"
                    v-for="(d, i) in departmentList"
                    :key="i"
                >
                    <q-card class="full-height bg-custom-card">
                        <q-card-section style="min-height: 120px">
                            <div class="text-h5 text-primary">
                                {{ `${d.name}` }}
                            </div>
                            <div class="text-caption text-secondary">
                                {{ d.faculty.name }}
                            </div>
                        </q-card-section>

                        <q-separator inset />
                        <q-card-actions
                            :align="$q.screen.xs ? 'center' : 'right'"
                            class="q-px-xs"
                        >
                            <div
                                class="q-ma-xs"
                                v-for="(b, i) in departmentBtnList"
                                :key="i"
                            >
                                <q-btn
                                    dark
                                    :outline="b.outline"
                                    :label="b.title"
                                    no-caps
                                    class="q-px-xs"
                                    color="primary"
                                    @click="onSelectDepartament(d, b.link)"
                                >
                                </q-btn>
                            </div>
                        </q-card-actions>
                    </q-card>
                </div>
            </q-card>

            <div
                :class="`col-md-3 col-sm-4 col-12 q-pt-lg ${
                    $q.screen.xs || 'q-pl-md'
                }`"
            >
                <q-card class="bg-custom-card" bordered>
                    <q-card-section class="q-mt-md">
                        <div
                            class="text-h5 text-bold row items-center justify-start"
                        >
                            Planificación de las tesis

                            <q-select
                                class="col-md-8 col-11 q-mt-xl q-mb-sm"
                                :options="optionsYears"
                                :loading="loadingYears"
                                v-model="currentYear"
                                clearable
                                outlined
                                hide-bottom-space
                                option-label="name"
                                option-value="id"
                                dense
                            ></q-select>
                        </div>
                        <div></div>
                    </q-card-section>
                    <q-separator inset />
                    <q-card-actions align="right">
                        <div
                            class="q-ma-xs"
                            v-for="(b, i) in thesisBtnList"
                            :key="i"
                        >
                            <q-btn
                                dark
                                :outline="b.outline"
                                :label="b.title"
                                no-caps
                                class="q-px-xs"
                                color="primary"
                                @click="onSelectYear(b.link)"
                            >
                            </q-btn>
                        </div>
                    </q-card-actions>
                </q-card>
            </div>

            <q-card
                :class="`col-12 bg-custom-grey-card text-grey-8 row q-pa-md q-mt-lg q-px-lg justify-${
                    $q.screen.xs ? 'center' : 'between'
                }`"
            >
                <div class="text-caption">
                    {{ 2022 }}. Todos los derechos reservados
                </div>
                <div class="text-caption">MATCOM. Universidad de La Habana</div>
            </q-card>
        </div>
    </q-page>
</template>

<script lang="ts">
import { departmentService, scholarYearService } from 'src/services';
import { defineComponent, ref } from 'vue';
import CSVDownload from '../components/csvDownload/CSVDownload.vue';
import { useDepartmentSession } from 'src/hooks/departmentSession';
import { DepartmentModel } from 'src/models/teachingAssignments/department.model';
import { useRouter } from 'vue-router';
import { LinkData } from 'src/models/linkData';

export default defineComponent({
    components: { CSVDownload },

    setup(props, { emit }) {
        const departmentBtnList: Array<LinkData> = [
            {
                title: 'Profesores',
                link: 'professors',
                outline: true,
            },
            {
                title: 'Asignaturas',
                link: 'subjects',
                outline: true,
            },
            {
                title: 'Planificación',
                link: 'subject-plannings',
                outline: true,
            },
            {
                title: 'Asignación',
                link: 'teaching-assignments',
            },
        ];

        const thesisBtnList: Array<LinkData> = [
            {
                title: 'Tesis',
                link: 'thesis',
                outline: true,
            },
            {
                title: 'Tribunales',
                link: 'thesis-committees',
                outline: true,
            },
            {
                title: 'Defensas',
                link: 'thesis-defenses',
            },
        ];

        const departmentList = ref<DepartmentModel[]>([]);
        departmentService.list().then((r) => {
            departmentList.value = r.data.results;
        });
        const R = useRouter();
        const { setDepartment } = useDepartmentSession();
        const currentYear = ref();
        const optionsYears = ref();

        const loadingYears = ref(true);
        scholarYearService
            .list()
            .then((r) => {
                optionsYears.value = r.data.results;
                r.data.results.map((x) => {
                    if (x.current_year) {
                        currentYear.value = x;
                    }
                });
            })
            .finally(() => {
                loadingYears.value = false;
            });

        const imageBg = require('src/assets/UH img.jpg');
        return {
            imageBg,
            departmentList,
            currentYear,
            loadingYears,
            optionsYears,
            departmentBtnList,
            thesisBtnList,
            onSelectDepartament(obj: DepartmentModel, routeName: string) {
                setDepartment(obj);
                R.push({ name: routeName });
            },
            onSelectYear(routeName: string) {
                if (currentYear.value?.id)
                    R.push({
                        name: routeName + '-id',
                        params: {
                            idC: currentYear.value.id,
                            Cname: currentYear.value.name,
                        },
                    });
                else {
                    R.push({
                        name: routeName,
                    });
                }
            },
        };
    },
});
</script>
