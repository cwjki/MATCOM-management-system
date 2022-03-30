import { quasarColumn } from 'src/models/base';
import { ref } from 'vue';

export const studentTable = () => {
  const options = ref<quasarColumn[]>([
    {
      name: 'name',
      required: true,
      label: 'Dessert (100g serving)',
      align: 'center',
      field: (row: any) => row.name,
      sortable: true,
    },
    {
      name: 'calories',
      align: 'center',
      label: 'Calories',
      field: 'calories',
      sortable: true,
    },
    { name: 'fat', label: 'Fat (g)', field: 'fat', sortable: true },
    { name: 'carbs', label: 'Carbs (g)', field: 'carbs' },
    { name: 'protein', label: 'Protein (g)', field: 'protein' },
    { name: 'sodium', label: 'Sodium (mg)', field: 'sodium' },
  ]);

  const rows = ref<any[]>([]);
  const loading = ref(true);
  setTimeout(() => {
    loading.value = false;
    rows.value = [
      {
        name: 'Frozen Yogurt',
        calories: 159,
        fat: 6.0,
        carbs: 24,
        protein: 4.0,
        sodium: 87,
        calcium: '14%',
        iron: '1%',
      },
      {
        name: 'Ice cream sandwich',
        calories: 237,
        fat: 9.0,
        carbs: 37,
        protein: 4.3,
        sodium: 129,
        calcium: '8%',
        iron: '1%',
      },
    ];
  }, 5000);

  return {
    options,
    loading,
    rows,
  };
};
