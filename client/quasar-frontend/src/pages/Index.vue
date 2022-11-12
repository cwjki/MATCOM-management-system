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
                        <div class="text-h6">Planificación de las tesis</div>
                    </q-card-section>

                    <q-separator dark inset />

                    <q-card-actions align="left">
                        <q-btn dark outline no-caps color="primary">
                            Administrar
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
import { departmentService } from 'src/services';
import { defineComponent, ref } from 'vue';
import CSVDownload from '../components/csvDownload/CSVDownload.vue';
import { useDepartamentSesion } from 'src/hooks/departamentSesion';
import { DepartmentModel } from 'src/models/teachingAssignments/department.model';
import { useRouter } from 'vue-router';
export default defineComponent({
    components: { CSVDownload },

    setup(props, { emit }) {
        const departamentList = ref<DepartmentModel[]>([]);
        departmentService.list().then((r) => {
            departamentList.value = r.data.results;
        });
        const R = useRouter();
        const { setDepartament } = useDepartamentSesion();
        return {
            departamentList,
            onSelectDepartament(obj: DepartmentModel, routeName: string) {
                setDepartament(obj);
                R.push({ name: routeName });
            },
        };
    },
});
</script>
