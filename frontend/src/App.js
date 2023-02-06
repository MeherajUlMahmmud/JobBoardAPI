import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/common_pages/landing/LandingPage";
import LoginPage from "./pages/auth_pages/LoginPage";
import SignUpPage from "./pages/auth_pages/SignUpPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<LandingPage />} />
        <Route path="/auth/login" element={<LoginPage />} />
        <Route path="/auth/sign-up" element={<SignUpPage />} />
        {/* <Route path="/auth/reset-password" element={<ResetPassword />} /> */}
        {/* <Route path="/demo" element={<DemoPage />} />
          <Route path="/courses/:subject" element={<CoursesPage />} />
          <Route path="/privacy-policy" element={<PrivacyPolicy />} />
          <Route path="/terms" element={<Terms />} />
          <Route path="/feedback" element={<FeedbackPage />} />
          <Route path="/team" element={<TeamPage />} />
          <Route path="/career" element={<CareerPage />} />
          <Route path="/career/:job_slug" element={<JobDetailsPage />} />
          <Route path="/career/:job_slug/apply" element={<JobApplyPage />} />

          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/my-courses" element={<MyCoursesPage />} />
          <Route path="/course/:courseId" element={<CourseDetailsPage />} />
          <Route
            path="/course/:courseId/:chapterId"
            element={<ChapterDetails />}
          />
          <Route path="/settings" element={<SettingsPage />} />
          <Route path="/:username" element={<ProfilePage />} />

          <Route path="/forms" element={<FormDashboard />} />
          <Route path="/forms/view/:formId" element={<FormViewPage />} />
          <Route
            path="/forms/review/:formId/:userId"
            element={<FormReviewPage />}
          />
          <Route
            path="/forms/response/:formId/:userId"
            element={<UserResponsePage />}
          />
          <Route
            path="/forms/response/:formId"
            element={<TeachersResponse />}
          /> */}
        {/* <Route path="/forms/answer/:formId" element={<FormAnswerPage />} />
          <Route path="/forms/action" element={<FormsLayout />}>
            <Route path="edit/:formId" element={<FormEditPage />} />
            <Route path="preview/:formId" element={<FormPreviewPage />} />
            <Route path="settings/:formId" element={<FormSettingsPage />} />
          </Route> */}

        {/* <Route
              path="career"
              element={<ModeratorCareerPage />}
            />
            <Route
              path="career/all"
              element={<AllCareer />}
            />
            <Route
              path="career/update/:id"
              element={<UpdateCareer />}
            />
            <Route
              path="career/create"
              element={<CreateCareer />}
            />
            <Route
              path="donors"
              element={<ModeratorDonorPage />}
            />
            <Route
              path="settings"
              element={<ModeratorSettingsPage />}
            />
            <Route
              path="feedbacks"
              element={<ModeratorFeedbacksPage />}
            /> 
          </Route>*/}
      </Routes>
    </Router>
  );
}

export default App;
