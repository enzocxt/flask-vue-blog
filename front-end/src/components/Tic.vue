<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Tic',
  data() {
    return {
      msg: ''
    }
  },
  created () {
    this.getMessage()
  },
  methods: {
    getMessage () {
      const path = 'http://localhost:5000/api/tic'
      axios.get(path)
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    }
  }
}
</script>