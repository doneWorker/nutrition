<script setup lang="ts">
import TriangleIcon from "~/assets/icons/triangle.svg?component";

definePageMeta({
  middleware: ["only-guests"],
  pageTransition: {
    name: "slide",
    mode: "in-out",
  },
});

// Particles effect
onMounted(() => {
  const elementsToAnimate =
    document.querySelectorAll<HTMLDivElement>(".bg > div");

  elementsToAnimate.forEach((element) => {
    const speed = Math.random() * 0.5 + 0.1;
    const range = Math.random() * 20 + 20;

    let xPosition = element.clientLeft;
    let yPosition = element.clientTop;

    function updateTransform() {
      const time = Date.now() / 1000;
      const x = Math.sin(time * speed) * range + xPosition;
      const y = Math.cos(time * speed) * range + yPosition;

      element.style.transform = `translate(${x}px, ${y}px)`;

      requestAnimationFrame(updateTransform);
    }

    updateTransform();
  });
});

const route = useRoute();

const isSignIn = computed(() => route.name === "auth-sign-in");
const isSignUp = computed(() => route.name === "auth-sign-up");

defineExpose({
  isSignIn,
  isSignUp,
});
</script>

<template>
  <VContainer fluid class="auth pa-0 h-screen">
    <VRow>
      <VCol
        no-gutters
        cols="7"
        tag="main"
        class="d-flex align-center overflow-hidden"
      >
        <NuxtPage />
      </VCol>
      <VCol no-gutters cols="5" tag="aside">
        <div class="bg">
          <div>
            <TriangleIcon />
          </div>
          <div />
          <div />
        </div>
        <ClientOnly>
          <Transition name="slide-up">
            <div v-if="isSignIn" class="helper">
              <h2>New Here?</h2>
              <p>
                Sign up and discover a great <br />amount of new opportunities!
              </p>

              <NuxtLink to="/auth/sign-up"
                ><VBtn
                  color="white"
                  size="x-large"
                  elevation="24"
                  class="text-capitalize rounded-pill px-16"
                  >Sign Up</VBtn
                ></NuxtLink
              >
            </div>
            <div v-else class="helper">
              <h2>Already have an account?</h2>
              <p>
                Welcome back dear User! We've missed you a lot, please sign in
                to your account to make us a little more happier ;)
              </p>
              <NuxtLink to="/auth/sign-in"
                ><VBtn
                  color="white"
                  size="x-large"
                  elevation="24"
                  class="text-capitalize rounded-pill px-16"
                  >Sign In</VBtn
                ></NuxtLink
              >
            </div>
          </Transition>
        </ClientOnly>
      </VCol>
    </VRow>
  </VContainer>
</template>

<style lang="scss">
@import "styles/global.scss";
@import "styles/variables.scss";

// Animations
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.5s ease-out;
}

.slide-up-enter-from {
  opacity: 0;
}

.slide-up-leave-to {
  opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
  position: absolute;
  transform: translateX(-100vw);
  opacity: 0;
  transition: all 0.7s;
}

.slide-enter-to {
  transform: translateX(0);
  opacity: 1;
}

.slide-leave-to {
  transform: translateX(100vw);
  opacity: 0;
}

// Components
.auth {
  h1,
  h2 {
    font-size: 60px;
    font-weight: 600;
  }

  & > * {
    height: 100%;
  }

  main {
    position: relative;

    .form-container {
      gap: 20px;

      .social {
        p {
          margin-bottom: 20px;

          text-align: center;
          font-size: 22px;
          font-weight: 700;
          color: #737373;
        }

        .buttons {
          gap: 15px;
        }
      }

      .or {
        font-weight: 700;
        font-size: 18px;
        line-height: 22px;
        color: rgba(0, 0, 0, 0.5);
        text-transform: uppercase;
      }

      .form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 20px;

        .field {
          width: 100%;

          .v-field {
            border: 2px solid transparent;
          }

          .v-field--error {
            border-color: #c3440d;
          }

          .v-field--focused {
            border-color: #31ab8b;
          }

          &:not(.v-input--error) .v-input__details {
            display: none;
          }

          .v-field,
          .field .v-field__outline__end,
          .v-input__control,
          .v-field input {
            box-shadow: none;
            border-radius: 55px !important;
          }

          input:-internal-autofill-selected {
            background-color: transparent !important;
          }
        }

        button {
          margin-top: 10px;

          color: white;
          background-color: #22a786;
        }
      }
    }
  }

  aside {
    position: relative;
    width: 40%;

    .helper {
      margin: auto;
      max-width: 75%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 40px;

      text-align: center;
      color: white;

      h2 {
        line-height: 1;
      }

      p {
        font-size: 28px;
        font-weight: 500;
      }
    }

    .bg {
      position: absolute;
      z-index: -1;
      width: 100%;
      height: 100%;

      background: linear-gradient(
        78.65deg,
        #39b790 7.61%,
        #38b595 31.61%,
        #37aea2 52.42%,
        #3aaba8 71.36%,
        #3ba8ad 89.84%
      );

      & > div {
        position: absolute;
      }

      div:nth-child(1) {
        top: 7%;
        left: 12%;
        width: 210px;
        height: 150px;
      }
      div:nth-child(2) {
        top: 45%;
        left: 40%;
        width: 350px;
        height: 350px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.1);
      }

      div:nth-child(3) {
        bottom: 2%;
        right: -15%;
        width: 250px;
        height: 250px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.1);
      }
    }
  }
}
</style>
