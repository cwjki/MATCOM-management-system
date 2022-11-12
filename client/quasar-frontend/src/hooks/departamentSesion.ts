import { DepartmentModel } from 'src/models/teachingAssignments/department.model';
import { computed, ref } from 'vue';

const key = 'jw_d';

export const useDepartamentSesion = () => {
    const setDepartament = (d: DepartmentModel) => {
        localStorage.setItem(key, JSON.stringify(d));
    };

    const getDepartament = (): DepartmentModel => {
        const d = localStorage.getItem(key);
        if (d != null) return JSON.parse(d) as DepartmentModel;
        return {
            id: 0,
            faculty: {
                id: 0,
                name: '',
            },
            name: '',
        };
    };

    const refresh = () => {
        departament.value = getDepartament();
    };

    const clear = () => {
        localStorage.removeItem(key);
    };

    const departament = ref(getDepartament());

    return {
        setDepartament,
        getDepartament,
        refresh,
        clear,
        departament,
    };
};
