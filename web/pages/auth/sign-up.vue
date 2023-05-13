<script lang="ts" setup>
import { useToast, POSITION } from "vue-toastification";

import "vue-toastification/dist/index.css";
import { useField, useForm } from "vee-validate";
import * as yup from "yup";

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
    .matches(
      /^(?=.*[!@#\$%\^&\*])/,
      "  Must Contain  One Special Case Character"
    ),
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
  await sleep(2000);
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
  <form class="form" validate-on="blur" @submit.prevent="onSubmit">
    <VTextField
      v-model="email.value.value"
      class="field"
      bg-color="#DEF5EF"
      type="email"
      placeholder="E-mail"
      variant="solo"
      :error-messages="email.errorMessage.value"
    />

    <VTextField
      v-model="password.value.value"
      class="field"
      bg-color="#DEF5EF"
      placeholder="Password"
      variant="solo"
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
      type="password"
      :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
      @paste="onPaste"
      @click:append-inner="showPassword = !showPassword"
      :error-messages="confirmPassword.errorMessage.value"
    />

    <VBtn
      type="submit"
      color="#22A786"
      :loading="isSubmitting"
      :disabled="!isFormValid"
      >Sign Up</VBtn
    >
  </form>
</template>
