import { defineNuxtPlugin } from "#app";

interface IAuthInterface {
  signIn: (values: SignInForm) => Promise<unknown>;
}

/** ApiInstance interface provides us with good typing */
interface IApiInstance {
  auth: IAuthInterface;
}

const call = (url: string, payload: any) => {};

interface SignInForm {
  email: string;
  password: string;
}

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig();
  const apiUrl = config.public.apiUrl;

  /** an object containing all repositories we need to expose */
  const modules: IApiInstance = {
    auth: {
      signIn: (values: SignInForm) =>
        $fetch(`${apiUrl}/auth/sign-in`, {
          method: "POST",
          body: values,
        }),
    },
  };

  return {
    provide: {
      api: modules,
    },
  };
});
