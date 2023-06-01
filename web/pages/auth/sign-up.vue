<script lang="ts" setup>
import { useToast, POSITION } from "vue-toastification";
import "vue-toastification/dist/index.css";
import { useField, useForm } from "vee-validate";
import * as yup from "yup";
import GoogleIcon from "~/assets/icons/google-logo.svg?component";
import { signUp } from "~/api/auth";

useHead({
  title: "Auth | Sign Up",
});

const showPassword = ref(false);

const validationSchema = yup.object().shape({
  email: yup.string().email("Not an Email").required("Email is required"),
  password: yup
    .string()
    .required("Password is required")
    .min(8, "Must be at least 8 characters")
    .max(50, "Must be at most 30 characters")
    .matches(/^\S+$/, "Must not contain spaces")
    .matches(/^(?=.*[a-z])/, " Must Contain One Lowercase Character")
    .matches(/^(?=.*[A-Z])/, "  Must Contain One Uppercase Character")
    .matches(/^(?=.*[0-9])/, "  Must Contain One Number Character")
    .matches(/^(?=.*[!@#$%^&*])/, "  Must Contain  One Special Case Character"),
  confirmPassword: yup
    .string()
    .required()
    .oneOf([yup.ref("password")], "Passwords do not match"),
});

interface SignUpForm {
  email: string;
  password: string;
  confirmPassword: string;
}

const { handleSubmit, errors, isSubmitting } = useForm<SignUpForm>({
  validationSchema,
});

const email = useField("email"),
  password = useField("password"),
  confirmPassword = useField("confirmPassword");

const isFormValid = computed(() => {
  return Object.keys(errors.value).length === 0;
});

const onSubmit = handleSubmit(async (values: SignUpForm) => {
  signUp(values);
});

const onPaste = (e: ClipboardEvent) => {
  e.preventDefault();
  const toast = useToast();
  toast.warning("You cannot paste into this field", {
    position: POSITION.TOP_LEFT,
  });
};

defineExpose({
  showPassword,
  email,
  password,
  confirmPassword,
  isFormValid,
  isSubmitting,
  onSubmit,
  onPaste,
});
</script>

<template>
  <VContainer fluid class="form-container d-flex v-col-auto flex-column w-100">
    <h1 class="text-center">Create Your Account</h1>

    <div class="social">
      <p>Using social networks</p>
      <div class="buttons d-flex justify-center">
        <ClientOnly>
          <vTooltip text="Google Sign-in">
            <template v-slot:activator="{ props }">
              <VBtn v-bind="props" width="48" height="48" icon rounded>
                <GoogleIcon width="32" height="32" />
              </VBtn>
            </template>
          </vTooltip>
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
        <VDivider class="mx-4 bold" /><span class="or">or</span
        ><VDivider class="mx-4" />
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
            variant="solo"
            density="comfortable"
            :error-messages="email.errorMessage.value"
          />

          <VTextField
            v-model="password.value.value"
            class="field"
            bg-color="#DEF5EF"
            placeholder="Password"
            variant="solo"
            density="comfortable"
            :type="showPassword ? 'text' : 'password'"
            :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append-inner="showPassword = !showPassword"
            :error-messages="password.errorMessage.value"
          />

          <VTextField
            v-model="confirmPassword.value.value"
            class="field"
            bg-color="#DEF5EF"
            placeholder="Confirm Password"
            variant="solo"
            density="comfortable"
            type="password"
            :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
            @paste="onPaste"
            @click:append-inner="showPassword = !showPassword"
            :error-messages="confirmPassword.errorMessage.value"
          />

          <VBtn
            type="submit"
            color="#22A786"
            density="default"
            size="x-large"
            class="text-capitalize rounded-pill px-16"
            :loading="isSubmitting"
            :disabled="!isFormValid"
            >Sign Up</VBtn
          >
        </VForm>
      </VCol>
    </VRow>
  </VContainer>
</template>
