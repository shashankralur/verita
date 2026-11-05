import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'

const HomePage = () => {
    return (
        <div>
            <Container>
                <Row>
                    <Col xs={12}>
                        <div className="homepage-content text-center mt-40">
                            <h1>Complete AI Tester | Create Bugs free app</h1>
                        </div>
                    </Col>
                </Row>
            </Container>
        </div>
    )
}

export default HomePage