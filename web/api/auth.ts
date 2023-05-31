export interface SignInPayload {
  email: string;
  password: string;
}

export const signIn = async (payload: SignInPayload) => {
  const resp: any = await $fetch("/api/auth/sign-in", {
    method: "POST",
    body: payload,
  });

  const respUsers: any = await $fetch("/api/users");

  if (resp?.success === true) {
    localStorage.setItem("me", JSON.stringify(resp.data));
  }
};
