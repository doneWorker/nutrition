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
      placeholder="password"
      variant="solo"
      :type="showPassword ? 'text' : 'password'"
      :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
      @click:append-inner="showPassword = !showPassword"
      :error-messages="password.errorMessage.value"
    />

    <VBtn
      type="submit"
      color="#22A786"
      :loading="isSubmitting"
      :disabled="!isFormValid"
      >Sign In</VBtn
    >
  </form>
</template>

<script lang="ts" setup>
import { useField, useForm } from "vee-validate";
import * as yup from "yup";
import { sleep } from "../../utils/sleep";

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
