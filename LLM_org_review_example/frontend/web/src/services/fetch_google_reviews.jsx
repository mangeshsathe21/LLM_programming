import api_client_handle from "../api/client";


const fetch_google_reviews = async(organization_name) => {
    const response = api_client_handle.get(
        `/fetch_google_reviews/organization/${organization_name}`
    )
    return response
};

export default fetch_google_reviews;