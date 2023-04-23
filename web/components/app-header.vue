<template>
  <header className="header">My custom header</header>
</template>

<style scoped lang="scss">
@import "../variables.scss";

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 66px;

  background-color: $primary-color;
  color: $white;
}
</style>
