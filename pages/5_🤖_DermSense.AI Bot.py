
import streamlit as st
import time

# new line for chatgpt
def print_line_by_line(text, speed=0.1):
    lines = text.split("\n")
    for line in lines:
        st.write(line)
        time.sleep(speed)


def get_recommendations(age, condition, blood_type):
    if age <= 18:
        return get_recommendations_for_children(condition, blood_type)
    else:
        return get_recommendations_for_adults(condition, blood_type)

def get_recommendations_for_children(condition, blood_type):
    if condition == "Vitiligo":
        recommendations = [
            "Children:",
            "<b>Treatment:</b>",
            "• Topical corticosteroids: Low potency.",
            "• Phototherapy: Narrowband UVB.",
            "• Emotional support and counseling.",
            "<b>Lifestyle Measures:</b>",
            "• Sun protection with high SPF.",
            "• Balanced diet rich in fruits, vegetables, and whole grains.",
            "• Avoid triggers like stress and trauma.",
            "• Mild topical treatments suitable for children.",
            "<b>Food Plan:</b>",
            "• Include foods rich in vitamins A, C, and E.",
            "• Encourage a variety of fruits and vegetables.",
            "• Ensure an adequate intake of dairy or alternatives for calcium."
        ]
        if blood_type == "A":
            recommendations.append("Consider incorporating soy-based proteins.")
        # Add conditions based on blood type for children
        return recommendations
    # Add similar conditions for other skin issues affecting children
    if condition == "Eczema":
        recommendations = [
            "Children with Eczema:",
            "<b>Treatment:</b>",
            "• Emollients and moisturizers are key.",
            "• Topical corticosteroids as prescribed by a dermatologist.",
            "• Identify and avoid potential triggers.",
            "<b>Lifestyle Measures:</b>",
            "• Use mild, fragrance-free skincare products.",
            "• Dress in breathable fabrics like cotton.",
            "• Keep nails short to minimize scratching.",
            "• Cool baths with mild soap can help.",
            "<b>Diet:</b>",
            "• No specific dietary restrictions for eczema are universally recommended.",
            "• Monitor for food triggers and allergies, especially in consultation with a pediatrician or allergist."
        ]
        if blood_type == "A":
            recommendations.append(
                "<b>Blood Type A:</b> Emphasize a plant-based diet with grains and avoid dairy. Include foods rich in antioxidants.")
        # Add conditions based on blood type for children with eczema
        return recommendations

    if condition == "Pigment Issues":
        recommendations = [
            "<b>Age-Specific Skincare for Even Skin Tone:</b>",
            "Children:",
            "• Skincare: Focus on gentle cleansing and moisturizing.",
            "• Sun Protection: Emphasize sun protection with hats and clothing.",
            "• Diet: Encourage a balanced diet with fruits, vegetables, and hydration."
        ]
        if blood_type == "A":
            recommendations.extend([
                "<b>Blood Type A:</b>",
                "• Focus on a plant-based diet with antioxidants.",
                "• Consider incorporating soy-based proteins."
            ])
        # Add conditions based on blood type for children with pigment issues
        return recommendations

def get_recommendations_for_adults(condition, blood_type):
    if condition == "Vitiligo":
        recommendations = [
            "<b>Adults:</b>",
            "<b>Treatment:</b>",
            "• Topical corticosteroids: Adjust potency based on affected areas.",
            "• Phototherapy: Narrowband UVB or PUVA.",
            "• Excimer laser for localized patches.",
            "• Depigmentation for widespread vitiligo.",
            "• Consider micropigmentation for cosmetic camouflage.",
            "<b>Lifestyle Measures:</b>",
            "• Sun protection with high SPF.",
            "• Stress management techniques.",
            "• Regular dermatologist check-ups.",
            "• Cosmetic solutions for self-esteem.",
            "<b>Food Plan:</b>",
            "• Balanced diet with a variety of fruits, vegetables, and whole grains.",
            "• Antioxidant-rich foods.",
            "• Consider foods high in copper, as copper is involved in melanin production.",
            "• Adequate protein intake from lean sources.",
            "• Individualized dietary recommendations based on blood type may be explored with a nutritionist.",
            "<b>Blood Type Considerations:</b>"
        ]
        if blood_type == "A":
            recommendations.extend([
                "<b>Blood Type A:</b>",
                "• Emphasize a plant-based diet with fruits, vegetables, and grains.",
                "• Consider incorporating soy-based proteins."
            ])
        elif blood_type == "B":
            recommendations.extend([
                "<b>Blood Type B:</b>",
                "• Balanced diet with a variety of foods.",
                "• Emphasize green vegetables, eggs, and low-fat dairy."
            ])
        elif blood_type == "AB":
            recommendations.extend([
                "<b>Blood Type AB:</b>",
                "• Combination of A and B type diets.",
                "• Include a variety of foods, focusing on balance."
            ])
        elif blood_type == "O":
            recommendations.extend([
                "<b>Blood Type O:</b>",
                "• Emphasize a high-protein diet with meat, fish, and vegetables.",
                "• Limit grains and dairy."
            ])
        # Add conditions based on blood type for adults
        return recommendations

    # Add similar conditions for other skin issues affecting adults
    if condition == "Eczema":
        recommendations = [
            "Adults with Eczema:",
            "<b>Treatment:</b>",
            "• Topical corticosteroids or calcineurin inhibitors as prescribed.",
            "• Systemic medications may be recommended in severe cases.",
            "• Identify and manage triggers.",
            "<b>Lifestyle Measures:</b>",
            "• Use fragrance-free, hypoallergenic skincare products.",
            "• Dress in comfortable, breathable clothing.",
            "• Manage stress, as it can exacerbate eczema symptoms.",
            "• Use humidifiers in dry environments.",
            "<b>Diet:</b>",
            "• Maintain a balanced diet with a focus on whole foods.",
            "• Consider an elimination diet under the guidance of a healthcare professional to identify potential triggers.",
            "• Stay hydrated."
        ]
        if blood_type == "A":
            recommendations.append(
                "<b>Blood Type A</b>: Emphasize a plant-based diet with grains and avoid dairy. Include foods rich in antioxidants.")
        elif blood_type == "B":
            recommendations.append(
                "<b>Blood Type B</b>: Balanced diet with a variety of foods. Emphasize green vegetables, eggs, and low-fat dairy.")
        elif blood_type == "AB":
            recommendations.append(
                "<b>Blood Type AB</b>: Combination of A and B type diets. Include a variety of foods, focusing on balance.")
        elif blood_type == "O":
            recommendations.append(
                "<b>Blood Type O</b>: Emphasize a high-protein diet with meat and fish. Limit grains and dairy.")
        # Add conditions based on blood type for adults with eczema
        return recommendations

    if condition == "Pigment Issues":
        recommendations = [
            "Age-Specific Skincare for Even Skin Tone:",
            "<b>Adults:</b>",
            "• Skincare: Include exfoliants and antioxidants in your routine.",
            "• Sun Protection: Prioritize sunscreen with at least SPF 30.",
            "• Diet: Maintain a diet rich in vitamins C and E, antioxidants, and copper.",
            "• Sun Protection: Continue vigilant sun protection to prevent age-related pigmentation.",
            "• Diet: Focus on nutrient-dense foods to support overall skin health.",
            "Skin Condition-Specific Recommendations:",
            "<b>Hyperpigmentation:</b>",
            "• Use targeted treatments with ingredients like hydroquinone, niacinamide, or retinoids.",
            "• Consider chemical peels or laser treatments under dermatologist guidance.",
            "<b>General Skin Health:</b>",
            "• Maintain a consistent skincare routine with emphasis on hydration and sun protection.",
            "<b>Blood Type Considerations:</b>",
            "• While the blood type diet lacks strong scientific evidence, here are general recommendations:"
        ]
        if blood_type == "A":
            recommendations.extend([
                "<b>Blood Type A:</b>",
                "• Focus on a plant-based diet with antioxidants.",
                "• Consider incorporating soy-based proteins."
            ])
        elif blood_type == "B":
            recommendations.extend([
                "<b>Blood Type B:</b>",
                "• Emphasize a balanced diet with green vegetables and low-fat dairy."
            ])
        elif blood_type == "AB":
            recommendations.extend([
                "<b>Blood Type AB:</b>",
                "• Combine aspects of A and B type diets for variety and balance."
            ])
        elif blood_type == "O":
            recommendations.extend([
                "<b>Blood Type O:</b>",
                "• Emphasize a high-protein diet with meat and fish.",
                "• Limit grains and dairy."
            ])
        recommendations.extend([
            "Important Notes:",
            "• Individual Variation: Responses to skincare and dietary changes vary. It's crucial to observe how your skin reacts and adjust accordingly.",
            "• Dermatologist Consultation: For personalized advice and potential prescription treatments, especially for pigmentation concerns.",
            "• Sun Protection: Regardless of age, condition, or blood type, consistent sun protection is key to prevent pigmentation issues."
        ])
        # Add conditions based on blood type for adults with pigment issues
        return recommendations

def main():
    st.title("Skin Health Advisor")

    age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
    condition = st.selectbox("Select a skin condition:", ["Vitiligo", "Eczema", "Pigment Issues"])
    blood_type = st.selectbox("Select your blood type:", ["A", "B", "AB", "O"])

    if st.button("Get Recommendations"):
        recommendations = get_recommendations(age, condition, blood_type)
        st.subheader("Recommendations:")
        for recommendation in recommendations:
            if not recommendation.startswith("<b>"):
                print_line_by_line(recommendation, speed=0.10)
            else:
                st.markdown(recommendation, unsafe_allow_html=True)
            time.sleep(0.5)

            # st.write(recommendation, unsafe_allow_html=True)  # Allow HTML for bold formatting

if __name__ == "__main__":
    main()
