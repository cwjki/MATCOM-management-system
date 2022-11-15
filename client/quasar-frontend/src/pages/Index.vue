<template>
    <q-page padding>
        <div flat class="row full-width justify-evenly items-center">
            <q-card flat class="col-5">
                <q-card-section>
                    <div class="text-h6">Sistema de gestión docente</div>
                    <div class="text-subtitle2">
                        para la facultad de Matemática y Computación de la UH
                    </div>
                </q-card-section>
            </q-card>
            <div class="col-7 q-pa-sm">
                <q-card>
                    <q-card-section>
                        <div class="text-h6 row items-center">
                            Planificación de las tesis
                            <q-select
                                :options="optionsYears"
                                :loading="loadingYears"
                                v-model="currentYear"
                                clearable
                                hide-bottom-space
                                option-label="name"
                                option-value="id"
                                class="col-lg-3 col-md-4 col-sm-6 col-12 q-ml-md"
                                dense
                            ></q-select>
                        </div>
                        <div></div>
                    </q-card-section>
                    <q-separator inset />
                    <q-card-actions align="left">
                        <q-btn
                            dark
                            outline
                            no-caps
                            class="q-px-md"
                            color="primary"
                            @click="onSelectYear('thesis')"
                        >
                            Tesis
                        </q-btn>
                        <q-btn
                            dark
                            outline
                            no-caps
                            class="q-px-md"
                            color="primary"
                            @click="onSelectYear('thesis-committees')"
                        >
                            Tribunales
                        </q-btn>
                        <q-btn
                            dark
                            outline
                            no-caps
                            class="q-px-md"
                            color="primary"
                            @click="onSelectYear('thesis-defenses')"
                        >
                            Defensas
                        </q-btn>
                    </q-card-actions>
                </q-card>
            </div>
            <div class="full-width q-my-md q-px-sm">
                <q-separator></q-separator>
            </div>
            <div class="row justify-center col-12">
                <div
                    class="col-md-3 col-sm-6 col-12 q-pa-sm"
                    v-for="(d, i) in departamentList"
                    :key="i"
                >
                    <q-card class="full-height">
                        <q-card-section style="min-height: 120px">
                            <div class="text-h5 text-primary">
                                {{ `${d.name}` }}
                            </div>
                            <div class="text-caption text-secondary">
                                {{ d.faculty.name }}
                            </div>
                        </q-card-section>

                        <q-separator inset />
                        <q-card-actions align="right">
                            <q-btn
                                dark
                                outline
                                no-caps
                                class="q-px-md"
                                color="primary"
                                @click="onSelectDepartament(d, 'subjects')"
                            >
                                Asignaturas
                            </q-btn>
                            <q-btn
                                dark
                                outline
                                no-caps
                                class="q-px-md"
                                color="primary"
                                @click="
                                    onSelectDepartament(d, 'subject-plannings')
                                "
                            >
                                Planificación
                            </q-btn>
                            <q-btn
                                dark
                                no-caps
                                class="q-px-md"
                                color="primary"
                                @click="
                                    onSelectDepartament(
                                        d,
                                        'teaching-assignments'
                                    )
                                "
                            >
                                Asignación
                            </q-btn>
                        </q-card-actions>
                    </q-card>
                </div>
            </div>
        </div>
    </q-page>
</template>

<script lang="ts">
import { departmentService, scholarYearService } from 'src/services';
import { defineComponent, ref } from 'vue';
import CSVDownload from '../components/csvDownload/CSVDownload.vue';
import { useDepartamentSesion } from 'src/hooks/departamentSesion';
import { DepartmentModel } from 'src/models/teachingAssignments/department.model';
import { useRouter } from 'vue-router';
import { route } from 'quasar/wrappers';
export default defineComponent({
    components: { CSVDownload },

    setup(props, { emit }) {
        const departamentList = ref<DepartmentModel[]>([]);
        departmentService.list().then((r) => {
            departamentList.value = r.data.results;
        });
        const R = useRouter();
        const { setDepartament } = useDepartamentSesion();
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
        return {
            departamentList,
            currentYear,
            loadingYears,
            optionsYears,
            onSelectDepartament(obj: DepartmentModel, routeName: string) {
                setDepartament(obj);
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
