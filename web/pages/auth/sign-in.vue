<script lang="ts" setup>
import { useField, useForm } from "vee-validate";
import * as yup from "yup";
import { sleep } from "../../utils/sleep";

useHead({
  title: "Auth | Sign In",
});

const showPassword = ref(false);

const validationSchema = yup.object().shape({
  email: yup.string().email("Not an Email").required("Email is required"),
  password: yup
    .string()
    .min(8, "Must be at least 8 characters")
    .max(50, "Must be at most 30 characters")
    .matches(/^\S+$/, "Must not contain spaces")
    .matches(/^(?=.*[a-z])/, " Must Contain One Lowercase Character")
    .matches(/^(?=.*[A-Z])/, "  Must Contain One Uppercase Character")
    .matches(/^(?=.*[0-9])/, "  Must Contain One Number Character")
    .matches(
      /^(?=.*[!@#\$%\^&\*])/,
      "  Must Contain  One Special Case Character"
    ),
});

interface SignInForm {
  email: string;
  password: string;
}

const { handleSubmit, errors, isSubmitting } = useForm<SignInForm>({
  validationSchema,
});

const email = useField("email", undefined, { initialValue: "" }),
  password = useField("password", undefined, { initialValue: "" });

const isFormValid = computed(() => {
  return Object.keys(errors.value).length === 0;
});

const onSubmit = handleSubmit(async (values: SignInForm) => {
  await sleep(2000);
  console.log("values", values);
});

defineExpose({
  showPassword,
  email: email.value,
  password: password.value,
  isFormValid,
  isSubmitting,
  onSubmit,
});
</script>

<template>
  <VContainer fluid class="form-container d-flex v-col-auto flex-column w-100">
    <h1 class="text-center">Login to Your Account</h1>

    <div class="social">
      <p>Using social networks</p>
      <div class="buttons d-flex justify-center">
        <ClientOnly>
          <v-tooltip text="Google Sign-in">
            <template v-slot:activator="{ props }">
              <button v-bind="props" class="social-button">
                <img alt="sign in with google" src="/svgs/google-logo.svg" />
              </button>
            </template>
          </v-tooltip>
        </ClientOnly>
      </div>
    </div>

    <VRow no-gutters justify="center">
      <VCol
        cols="10"
        lg="7"
        xl="4"
        xxl="3"
        align-self="center"
        class="d-flex align-center ma-0"
      >
        <v-divider class="mx-4 bold"></v-divider><span class="or">or</span
        ><v-divider class="mx-4"></v-divider>
      </VCol>
    </VRow>

    <VRow no-gutters justify="center">
      <VCol cols="10" lg="7" xl="4" xxl="3" align-self="center">
        <VForm class="form pa-0" validate-on="blur" @submit.prevent="onSubmit">
          <VTextField
            v-model="email.value.value"
            class="field"
            bg-color="#DEF5EF"
            type="email"
            placeholder="E-mail"
            density="comfortable"
            variant="solo"
            :error-messages="email.errorMessage.value"
          />

          <VTextField
            v-model="password.value.value"
            class="field"
            bg-color="#DEF5EF"
            placeholder="password"
            variant="solo"
            density="comfortable"
            :type="showPassword ? 'text' : 'password'"
            :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append-inner="showPassword = !showPassword"
            :error-messages="password.errorMessage.value"
          />

          <VBtn
            type="submit"
            color="#22A786"
            density="default"
            size="x-large"
            class="text-capitalize rounded-pill px-16"
            :loading="isSubmitting"
            :disabled="!isFormValid"
            >Sign In</VBtn
          >
        </VForm>
      </VCol>
    </VRow>
  </VContainer>
</template>
