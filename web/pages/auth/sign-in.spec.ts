import { describe, it, expect } from "vitest";
import { mount } from "@vue/test-utils";

import SignIn from "./sign-in.vue";

describe("SignIn", () => {
  it("is a Vue instance", () => {
    const wrapper = mount(SignIn);
    expect(wrapper.vm).toBeTruthy();
  });
});
