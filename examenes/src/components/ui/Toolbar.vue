<template lang="es">
    <div class="font-sans bg-sky-500 rounded-b-lg p-3 flex-wrap sm:flex gap-3">
        <h1 class='text-2xl font-medium p-2 animation ease-in-out duration-500 hover:text-emerald-200 hover:scale-110 hover:cursor-pointer'>
            {{datos.titulo}}
        </h1>
        <div class="grow">
            <nav>
                <ul class='flex gap-3 text-sky-800'>
                    <li class="shadow-md rounded-lg p-2 animation ease-in-out duration-150 hover:translate-y-1 hover:shadow-none" v-for="(item, index) in datos.enlaces" :key="index">
                        {{item}}
                    </li>
                </ul>
            </nav>
        </div>
        <div>
            <nav>
                <ul class='flex gap-3 text-gray-200'>
                    <li class="shadow-md rounded-lg p-2 bg-emerald-600 animation ease-in-out duration-150 hover:translate-y-1 hover:shadow-none" v-for="(item, index) in datos.primarios" :key="index">
                        {{item}}
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Toolbar',
    props: {
        datos: {
            type: Object,
            required: true
        }
    },
}
</script>