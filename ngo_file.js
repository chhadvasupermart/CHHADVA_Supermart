import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { motion } from "framer-motion";

export default function StartupApp() {
  const [formData, setFormData] = useState({ name: "", email: "", message: "" });
  
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitted Data:", formData);
  };

  return (
    <div className="p-10 max-w-4xl mx-auto">
      <motion.h1 className="text-3xl font-bold text-center mb-6" animate={{ scale: 1.1 }}>AI & Biotech Startup</motion.h1>
      <Card className="p-6 shadow-lg rounded-xl">
        <CardContent>
          <p className="text-lg mb-4">We specialize in AI-driven learning, biotech research, semiconductor advancements, and educational technology.</p>
          <h2 className="text-xl font-semibold">Contact Us</h2>
          <form onSubmit={handleSubmit} className="flex flex-col gap-4 mt-4">
            <Input type="text" name="name" placeholder="Your Name" value={formData.name} onChange={handleChange} required />
            <Input type="email" name="email" placeholder="Your Email" value={formData.email} onChange={handleChange} required />
            <Textarea name="message" placeholder="Your Message" value={formData.message} onChange={handleChange} required />
            <Button type="submit" className="bg-blue-500 text-white hover:bg-blue-700">Submit</Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
