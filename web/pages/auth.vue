<script setup lang="ts">
definePageMeta({
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
  <div class="auth">
    <main>
      <div class="form-container d-flex v-col-auto flex-column">
        <ClientOnly>
          <Transition>
            <h1 v-if="isSignIn">Login to Your Account</h1>
            <h1 v-else>Create Your Account</h1>
          </Transition>
        </ClientOnly>

        <div class="social">
          <p>Using social networks</p>
          <div class="buttons d-flex justify-center">
            <ClientOnly>
              <v-tooltip text="Google Sign-in">
                <template v-slot:activator="{ props }">
                  <button v-bind="props" class="social-button">
                    <img
                      alt="sign in with google"
                      src="/svgs/google-logo.svg"
                    />
                  </button>
                </template>
              </v-tooltip>
            </ClientOnly>
          </div>
        </div>
        <VContainer class="d-flex align-center">
          <v-divider class="mx-4 bold"></v-divider><span class="or">or</span
          ><v-divider class="mx-4"></v-divider>
        </VContainer>

        <NuxtPage />
      </div>
    </main>
    <aside>
      <div class="bg">
        <div>
          <svg
            width="203"
            height="200"
            viewBox="0 0 203 200"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M106 0.499988L202.087 126.651L0.729406 199.939L106 0.499988Z"
              fill="white"
              fill-opacity="0.1"
            />
          </svg>
        </div>
        <div></div>
        <div></div>
      </div>
      <ClientOnly>
        <div v-show="isSignIn" class="helper">
          <h2>New Here?</h2>
          <p>Sign up and discover a great <br />amount of new opportunities!</p>
          <NuxtLink to="/auth/sign-up"
            ><VBtn class="side-button">Sign Up</VBtn></NuxtLink
          >
        </div>
        <div v-show="isSignUp" class="helper">
          <h2>Already have an account?</h2>
          <p>
            Welcome back dear User! We've missed you a lot, please sign in to
            your account to make us a little more happier ;)
          </p>
          <NuxtLink to="/auth/sign-in"
            ><VBtn class="side-button">Sign In</VBtn></NuxtLink
          >
        </div>
      </ClientOnly>
    </aside>
  </div>
</template>

<style lang="scss">
@import "../styles/global.scss";
@import "../styles/variables.scss";

.slide-enter-active,
.slide-leave-active {
  position: absolute;
  transform: translateX(-100vw);
  opacity: 0;
  transition: all 1s;
}
.slide-enter-to {
  transform: translateX(0);
  opacity: 1;
}

.slide-leave-to {
  transform: translateX(100vw);
  opacity: 0;
}

.auth {
  overflow: hidden;
  width: 100vw;
  height: 100vh;
  display: flex;

  h1,
  h2 {
    font-size: 60px;
    font-weight: 600;
  }

  & > * {
    height: 100%;
  }

  main {
    width: 60%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

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

          .social-button {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 48px;
            height: 48px;
            border-radius: 50%;
            box-shadow: 0 0 2px $green-500;

            img {
              width: 75%;
            }
          }
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
          width: 530px;

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
          .v-input__control {
            box-shadow: none;
            border-radius: 55px !important;
          }
        }

        button {
          align-self: center;
          height: auto;
          padding: 18px 100px;
          margin-top: 10px;

          text-transform: capitalize;
          font-size: 20px;
          border-radius: 50px;
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

      .side-button {
        height: auto;
        padding: 18px 100px;
        text-transform: capitalize;

        font-size: 20px;
        font-weight: 600;
        border-radius: 45px;
        background-color: white;
        color: black;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.25);
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
