import { Notify } from 'quasar';
import { ref } from 'vue';

export const Logger = () => {
  const s = ref<string>('');
  return {
    s,
    log() {
      // alert(s.value);
      Notify.create({
        message: s.value,
        type: 'positive',
      });
    },
  };
};
