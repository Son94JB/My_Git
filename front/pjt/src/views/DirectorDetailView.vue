<template>
  <div>
    <h1>{{ directorDetail.name }}</h1>
  </div>
</template>

<script>
export default {
    name: 'DirectorDetailView',
    computed: {
        directorDetail() {
        return this.$store.getters.directorDetail;
        },
    },
    created() {
        this.$store.dispatch('fetchDirectorDetail', this.$route.params.id);
    },
}
</script>

<style>

</style>