<template>
  <div>
    <p @click="onClickBtn">{{ title }} {{ s }}</p>
    <ul>
      <li v-for="todo in todos" :key="todo.id" @click="increment">
        {{ todo.id }} - {{ todo.content }}
      </li>
    </ul>
    <p>Count: {{ todoCount }} / {{ meta.totalCount }}</p>
    <p>Active: {{ active ? 'yes' : 'no' }}</p>
    <p>Clicks on todos: {{ clickCount }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, computed, ref, toRef, Ref } from 'vue';
import { Todo, Meta } from './models';
import { Logger } from 'src/hooks/basic.hooks';

function useClickCount() {
  const clickCount = ref(0);
  function increment() {
    clickCount.value += 1;
    return clickCount.value;
  }

  return { clickCount, increment };
}

function useDisplayTodo(todos: Ref<Todo[]>) {
  const todoCount = computed(() => todos.value.length);
  return { todoCount };
}

export default defineComponent({
  name: 'ExampleComponent',
  props: {
    title: {
      type: String,
      required: true,
    },
    todos: {
      type: Array as PropType<Todo[]>,
      default: () => [],
    },
    meta: {
      type: Object as PropType<Meta>,
      required: true,
    },
    active: {
      type: Boolean,
    },
  },
  emits: ['onClick'],
  setup(props, { emit }) {
    const { log, s } = Logger();
    s.value = 'Hola mundo';
    log();
    const { clickCount, increment } = useClickCount();
    return {
      clickCount,
      increment,
      s,
      log,
      ...useDisplayTodo(toRef(props, 'todos')),
      onClickBtn() {
        s.value += ' a';
        emit('onClick', s.value);
      },
    };
  },
});
</script>
