import { DepartmentModel } from 'src/models/teachingAssignments/department.model';
import { ref } from 'vue';

const key = 'jw_d';

export const useDepartmentSession = () => {
    const setDepartment = (d: DepartmentModel) => {
        localStorage.setItem(key, JSON.stringify(d));
    };

    const getDepartment = (): DepartmentModel => {
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
        department.value = getDepartment();
    };

    const clear = () => {
        localStorage.removeItem(key);
        document.location.reload();
    };

    const department = ref(getDepartment());

    return {
        setDepartment,
        getDepartment,
        refresh,
        clear,
        department,
    };
};
