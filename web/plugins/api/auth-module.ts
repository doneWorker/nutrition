class AuthModule {
  private RESOURCE = "/auth";

  async login(credentials: ILoginInput): Promise<ILoginResponse> {
    return await this.call<ILoginResponse>(
      "POST",
      `${this.RESOURCE}/login`,
      credentials
    );
  }
}

export default AuthModule;
