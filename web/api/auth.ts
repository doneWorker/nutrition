export interface SignInPayload {
  email: string;
  password: string;
}

export const signIn = async (payload: SignInPayload) => {
  const resp: any = await $fetch("/api/auth/sign-in", {
    method: "POST",
    body: payload,
  });

  if (resp?.success === true) {
    localStorage.setItem("me", JSON.stringify(resp.data));
  }

  window.location.reload();
};

export interface SignUpPayload {
  email: string;
  password: string;
  confirmPassword: string;
}

export const signUp = async (payload: SignUpPayload) => {
  const resp: any = await $fetch("/api/auth/sign-up", {
    method: "POST",
    body: {
      email: payload.email,
      password: payload.password,
      confirm_password: payload.confirmPassword,
    },
  });

  if (resp?.success === true) {
    localStorage.setItem("me", JSON.stringify(resp.data));
  }

  window.location.reload();
};

export const signOut = async () => {
  const resp: any = await $fetch("/api/auth/sign-out", {
    method: "POST",
  });

  if (resp?.success === true) {
    localStorage.removeItem("me");
  }

  window.location.reload();
};
